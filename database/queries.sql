select
    company_name,
    f.change
from company_information
inner join 
(
    select 
        market_data.company_id,
        change
    from market_data
    inner join (
        select 
            max(stock_date) as stock_date,
            company_id
        from market_data
        group by company_id
    ) as f on 
        f.company_id=market_data.company_id and f.stock_date=market_data.stock_date
) as f on
    f.company_id=company_information.company_id;


