Question 1:
a (i)cityIn(london, uk).
a (ii)iVisited(strasbourg).
b  chile, argentuna.
c  countriesIVisited(Country) IF cityIn(City, Country) AND iVisited(City).

Question 2: 
a (i)  Emma has license.
a (ii)
allowedToDrive(X, V)
	IF hasLicense(X) AND minimumAge(V, L)
		AND age(X, A)
		AND A >= L.
b (i)  Who = jack
b (ii)  false
b (iii) false
c (i) qualifiedCarDrivers(T) IF qualifiedDriver(T, car).
c (ii) partQualified(X)IF passedTheoryTest(X) AND NOT passedDrivingTest(X, _).
d  Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A as 17), clause 15 ( A >= L is false) result is false.