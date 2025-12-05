location(chennai, tamilnadu).
location(madurai, tamilnadu).
location(mumbai, maharashtra).
location(pune, maharashtra).
location(hyderabad, telangana).

stays(ravi, chennai).
stays(asha, mumbai).
stays(kumar, hyderabad).
stays(sita, pune).
stays(rajesh, madurai).

display(Person, City, State) :-
	stays(Person, City),
	location(City, State).
state_of_person(Person, State) :-
	stays(Person, City),
	location(City, State).