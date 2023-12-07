male(kankavee).
male(kiatkarun).
male(jityut).
male(sontaya).
male(tharathip).
male(prayong).
male(chueb).
female(patcharee).
female(wassana).
female(nichada).
female(manee).
female(sun).

father(jityut,kankavee).
father(jityut,kiatkarun).
father(sontaya,tharathip).
father(prayong,jityut).
father(prayong,sontaya).
father(chueb,patcharee).
father(chueb,wassana).

mother(patcharee,kankavee).
mother(patcharee,kiatkarun).
mother(wassana,nichada).
mother(manee,jityut).
mother(manee,sontaya).
mother(sun,patcharee).
mother(sun,wassana).


/* Rules */

parents(A,B):-father(A,B).
parents(A,B):-mother(A,B).
grandfather(A,B):-male(A),parents(A,C),parents(C,B).
grandmother(A,B):-female(A),parents(A,C),parents(C,B).

sibling(A,B):-parents(C,B),parents(C,A).

brother(A,B):-male(A),father(C,B),father(C,A),A \= B.
brother(A,B):-male(A),mother(C,B),mother(C,A),A \= B.
sister(A,B):-male(A),father(C,B),father(C,A),A \= B.
sister(A,B):-male(A),mother(C,B),mother(C,A),A \= B.

cousin(A,B):-grandfather(C,A) , grandfather(C,B) ,  father(D,A) , father(F,B) ,F\=D , D\=F.















    








    










    




