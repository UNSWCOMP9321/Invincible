CREATE TABLE JOB_AU(
    category    VARCHAR(150),
    city    VARCHAR(50),
    company     VARCHAR(100),
    job_type    VARCHAR(50)
);
CREATE INDEX JOB_AU_index_city ON JOB_AU (city);

CREATE TABLE JOB_UK(
    category    VARCHAR(150),
    city    VARCHAR(50),
    company     VARCHAR(100),
    job_type    VARCHAR(50)
);
CREATE INDEX JOB_UK_index_city ON JOB_UK (city);


--industry job amount
CREATE TABLE CATE_AU(
    category        VARCHAR(150),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    PRIMARY KEY(category)
);

CREATE TABLE CATE_UK(
    category        VARCHAR(150),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    PRIMARY KEY(category)
);

--city job amount
CREATE TABLE CITY_AU(
    city            VARCHAR(50),
    longitude       NUMERIC(7,4),
    latitude        NUMERIC(7,4),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    company_amount  INTEGER,
    company_ratio   NUMERIC(5,2),
    PRIMARY KEY(city, longitude, latitude)
);

CREATE TABLE CITY_UK(
    city            VARCHAR(50),
    longitude       NUMERIC(7,4),
    latitude        NUMERIC(7,4),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    company_amount  INTEGER,
    company_ratio   NUMERIC(5,2),
    PRIMARY KEY(city, longitude, latitude)
);

--company job amount
CREATE TABLE COMP_AU(
    company             VARCHAR(100),
    company_amount      INTEGER,
    company_ratio       NUMERIC(5,2),
    PRIMARY KEY(company)
);

CREATE TABLE COMP_UK(
    company             VARCHAR(100),
    company_amount      INTEGER,
    company_ratio       NUMERIC(5,2),
    PRIMARY KEY(company)
);

--parttime/fulltime job amount
CREATE TABLE JOB_TYPE_AU(
    job_type        VARCHAR(50),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    PRIMARY KEY(job_type)
);

CREATE TABLE JOB_TYPE_UK(
    job_type        VARCHAR(50),
    job_amount      INTEGER,
    job_ratio       NUMERIC(5,2),
    PRIMARY KEY(job_type)
);

--weekly work hours
CREATE TABLE WORK_HOURS(
    country     VARCHAR(2),
    sex         VARCHAR(10),
    category    VARCHAR(150),
    hours       INTEGER,
    PRIMARY KEY(country,sex,category)
);