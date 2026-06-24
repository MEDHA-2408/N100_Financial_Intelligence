SELECT COUNT(*) FROM financial_ratios;

SELECT company_id,
AVG(return_on_equity_pct)
FROM financial_ratios
GROUP BY company_id
ORDER BY AVG(return_on_equity_pct) DESC;

SELECT company_id,
AVG(net_profit_margin_pct)
FROM financial_ratios
GROUP BY company_id
ORDER BY AVG(net_profit_margin_pct) DESC;

SELECT company_id,
MAX(health_score_v2)
FROM financial_ratios
GROUP BY company_id;

SELECT year,
AVG(return_on_equity_pct)
FROM financial_ratios
GROUP BY year;