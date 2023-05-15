select
    company_name,
    f.change,
    f.stock_date
from company_information
inner join 
(
    select 
        market_data.company_id,
        change,
        f.stock_date
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


select user_id
from auth
where email_id='{email}' and pass='{password}';





select
    *
from company_information
where company_name='{company_name}';

            select
                company_name,
                f.close_price,
                f.change,
                f.company_id
            from company_information
            inner join
            (
                select
                    market_data.company_id,
                    close_price,
                    change
                from market_data
                inner join (
                    select
                        company_id
                    from watchlist
                    where user_id=2
                ) as g on g.company_id=market_data.company_id
                inner join (
                    select
                        max(stock_date) as stock_date,
                        company_id
                    from market_data
                    group by company_id
                ) as f on
                    f.company_id=market_data.company_id and f.stock_date=market_data.stock_date
            ) as f on
                f.company_id = company_information.company_id;

select
    company_id,
    max(stock_date),
    close_price,
    change
from market_data
group by company_id;

