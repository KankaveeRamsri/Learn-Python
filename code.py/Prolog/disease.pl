
run :- 
	hypothesis(Disease),
	write('I believe that the patient has'), nl,
	write(' --- '), 
	write(Disease), write(' --- '), nl,
	write('Take care :)'),
	clear.


hypothesis(covid) :- covid, !.
hypothesis(cold) :- cold, !.
hypothesis(sinus) :- sinus, !.
hypothesis(malaria) :- malaria, !.
hypothesis(influenza) :- influenza, !.

hypothesis(unknown).

covid :- 
	verify(fever),
	verify(dry_cough),
	verify(loss_sense_of_smell),
	verify(shortness_of_breath),
	write('Advices and Suggestions:'), nl,
	write('  ** Quarantine for two weeks'), nl.
	
cold :- 
	verify(headache),
	verify(sneezing),
	verify(runny_nose),
	verify(sore_throath),	
	write('Advices and Suggestions:'), nl,
	write('  1: Paracetamol/tab'), nl,
	write('  2: Tylenol/tab'), nl,
	write('  3: Nasal spray'), nl,
	write('  ** Please wear warm cloths'), nl.

malaria :-
	verify(fever),
	verify(headache),
	verify(sweating),
	verify(vomiting),
	verify(nausea),
	verify(diarrhea),
	write('Advices and Suggestions:'), nl,
	write('  1: Aralen/tab'), nl,
	write('  2: Qualaquin/tab'), nl,
	write('  3: Mefloquine'), nl,
	write('  ** Please do not sleep in open air and cover your full skin'), nl.

sinus :-
	verify(runny_nose),
	verify(loss_sense_of_smell),
	verify(shortness_of_breath),
	verify(coughing),
	verify(headache),
	verify(toothache),
	write('Advices and Suggestions:'), nl,
	write('  ** Please go to see a doctor'), nl.

influenza :-
    verify(fever),
    verify(aching_muscles),
    verify(chills_and_sweats),
    verify(headache),
    verify(dry_and_persistent_cough),
    verify(shortness_of_breath),
    verify(tiredness_and_weakness),
    verify(runny_or_stuffy_nose),
    write('Advices and Suggestions:'), nl,
    write('  ** Please go to see a doctor'), nl.
    	

ask(Question) :-
	write('Does the patient have following symthom: '),
	write(Question),
	write('(y/n)? '),
	read(Response),nl,
	((Response == y) -> assert(yes(Question)) ;
					    assert(no(Question)), fail).

:- dynamic (yes/1).
:- dynamic (no/1).

verify(S) :-
	(yes(S) -> true;
	(no(S) -> fail;
	ask(S))).
	

clear :- retractall(yes(_)), retractall(no(_)); true.
clear.