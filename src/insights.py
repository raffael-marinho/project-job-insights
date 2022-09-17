from src.jobs import read


def get_unique_job_types(path):
    readed = read(path)
    jobTypes = []
    for job in readed:
        if job["job_type"] not in jobTypes:
            jobTypes.append(job["job_type"])
    return jobTypes


# jobs.filter((job) => job === "programador")
def filter_by_job_type(jobs, job_type):
    return list(filter(lambda job: job["job_type"] == job_type, jobs))


def get_unique_industries(path):
    readed = read(path)
    industryTypes = []
    for industry in readed:
        if industry["industry"] != "":
            if industry["industry"] not in industryTypes:
                industryTypes.append(industry["industry"])
    return industryTypes


def filter_by_industry(jobs, industry):
    return list(filter(lambda job: job["industry"] == industry, jobs))


def get_max_salary(path):
    readed = read(path)
    salaryTypes = []
    for salary in readed:
        if salary["max_salary"] != "":
            if salary["max_salary"] != "invalid":
                salaryTypes.append(int(salary["max_salary"]))
    return max(salaryTypes)


def get_min_salary(path):
    readed = read(path)
    salaryTypes = []
    for salary in readed:
        if salary["min_salary"] != "":
            if salary["min_salary"] != "invalid":
                salaryTypes.append(int(salary["min_salary"]))
    return min(salaryTypes)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
