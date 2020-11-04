CREATE TABLE IF NOT EXISTS public.GlobalLandTemperaturesByCountry (
	dt DATE NOT NULL,
	AverageTemperature FLOAT,
	AverageTemperatureUncertainty FLOAT,
	Country VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS public.GlobalLandTemperaturesByState (
	dt DATE NOT NULL,
	AverageTemperature FLOAT,
	AverageTemperatureUncertainty FLOAT,
    State VARCHAR(255),
	Country VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS public.HappinessRanksByCountry (
	OverallRank INT NOT NULL,
	Country VARCHAR(255),
	Score FLOAT,
    GDPPerCapita FLOAT,
	SocialSupport FLOAT,
    LifeExpectancy FLOAT,
    Freedom FLOAT,
    Generosity FLOAT,
    Corruption FLOAT
);

CREATE TABLE IF NOT EXISTS public.CountryNames (
	CountryAbbreviation VARCHAR(255),
    CountryName VARCHAR(255)
    );

