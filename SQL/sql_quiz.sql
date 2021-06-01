-- 직원의 이름(FIRST_NAME)과 부서명(DEPARTMENT_NAME) 그리고 근무지(CITY)를 부서명으로 오름차순하여 출력하시오. 
-- (null data도 포함해서 출력)

select e.first_name, d.department_name, l.city
from employees e, departments d, locations l
where e.department_id = d.department_id and d.location_id = l.location_id
	order by department_name asc;

-- 근무지(CITY)별 직원의 수를 직원 수를 기준으로 내림차순하여 출력하시오

select l.city, count(e.first_name)
from employees e, departments d, locations l
where e.department_id = d.department_id and d.location_id = l.location_id
group by l.city
	order by count(e.first_name) desc;