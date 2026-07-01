#!/usr/bin/env python3
"""Restaurant break-even and runway calculator for yongge-catering-skill."""

import argparse
import json
import sys


def pct(value):
    if value is None:
        return None
    if value > 1:
        return value / 100
    return value


def money(value):
    return f"{value:,.0f}"


def calculate(args):
    days = args.business_days
    monthly_sales = args.daily_sales * days if args.daily_sales is not None else args.monthly_sales

    fixed = sum(
        x or 0
        for x in [
            args.rent,
            args.property_fee,
            args.labor,
            args.utilities,
            args.loan_payment,
            args.marketing,
            args.other_fixed,
        ]
    )

    gross_margin = pct(args.gross_margin)
    food_cost_rate = pct(args.food_cost_rate)
    platform_rate = pct(args.platform_rate) or 0
    packaging_rate = pct(args.packaging_rate) or 0
    discount_rate = pct(args.discount_rate) or 0
    waste_rate = pct(args.waste_rate) or 0

    if gross_margin is None:
        if food_cost_rate is None:
            raise SystemExit("Provide --gross-margin or --food-cost-rate.")
        gross_margin = 1 - food_cost_rate

    contribution = gross_margin - platform_rate - packaging_rate - discount_rate - waste_rate
    if contribution <= 0:
        raise SystemExit("Contribution margin is <= 0 after costs. The model cannot break even.")

    break_even_monthly = fixed / contribution
    break_even_daily = break_even_monthly / days

    profit = None
    gap_daily = None
    runway_months = None
    if monthly_sales is not None:
        profit = monthly_sales * contribution - fixed
        gap_daily = break_even_daily - (monthly_sales / days)
        if args.cash is not None and profit < 0:
            runway_months = args.cash / abs(profit) if profit else None

    return {
        "business_days": days,
        "monthly_fixed_cost": fixed,
        "contribution_margin_rate": contribution,
        "break_even_monthly_sales": break_even_monthly,
        "break_even_daily_sales": break_even_daily,
        "monthly_sales": monthly_sales,
        "estimated_monthly_profit": profit,
        "daily_sales_gap_to_break_even": gap_daily,
        "cash_runway_months": runway_months,
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate restaurant break-even and runway.")
    parser.add_argument("--daily-sales", type=float, help="Average daily sales/revenue.")
    parser.add_argument("--monthly-sales", type=float, help="Monthly sales/revenue.")
    parser.add_argument("--business-days", type=int, default=30)
    parser.add_argument("--rent", type=float, default=0)
    parser.add_argument("--property-fee", type=float, default=0)
    parser.add_argument("--labor", type=float, default=0)
    parser.add_argument("--utilities", type=float, default=0)
    parser.add_argument("--loan-payment", type=float, default=0)
    parser.add_argument("--marketing", type=float, default=0)
    parser.add_argument("--other-fixed", type=float, default=0)
    parser.add_argument("--gross-margin", type=float, help="Gross margin rate, e.g. 0.55 or 55.")
    parser.add_argument("--food-cost-rate", type=float, help="Food cost rate, e.g. 0.35 or 35.")
    parser.add_argument("--platform-rate", type=float, default=0)
    parser.add_argument("--packaging-rate", type=float, default=0)
    parser.add_argument("--discount-rate", type=float, default=0)
    parser.add_argument("--waste-rate", type=float, default=0)
    parser.add_argument("--cash", type=float, help="Remaining available cash.")
    parser.add_argument("--json", action="store_true", help="Output JSON only.")
    args = parser.parse_args()

    result = calculate(args)
    if args.json:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return

    print("餐饮保本线测算")
    print(f"- 月固定成本：{money(result['monthly_fixed_cost'])}")
    print(f"- 贡献毛利率：{result['contribution_margin_rate']:.1%}")
    print(f"- 月保本流水：{money(result['break_even_monthly_sales'])}")
    print(f"- 日保本流水：{money(result['break_even_daily_sales'])}")
    if result["monthly_sales"] is not None:
        print(f"- 当前月流水：{money(result['monthly_sales'])}")
        print(f"- 预估月利润：{money(result['estimated_monthly_profit'])}")
        print(f"- 距离日保本差额：{money(result['daily_sales_gap_to_break_even'])}")
    if result["cash_runway_months"] is not None:
        print(f"- 现金还能撑：{result['cash_runway_months']:.1f} 个月")


if __name__ == "__main__":
    main()
