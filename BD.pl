estudiante(juan).
estudiante(maria).
estudiante(pedro).
estudiante(laura).
estudiante(carlos).

asignatura(matematicas).
asignatura(fisica).
asignatura(quimica).
asignatura(literatura).
asignatura(historia).

calificacion(juan, matematicas, 95).
calificacion(juan, fisica, 89).
calificacion(juan, quimica, 76).
calificacion(juan, literatura, 84).
calificacion(juan, historia, 91).

calificacion(maria, matematicas, 88).
calificacion(maria, fisica, 95).
calificacion(maria, quimica, 70).
calificacion(maria, literatura, 90).
calificacion(maria, historia, 85).

calificacion(pedro, matematicas, 75).
calificacion(pedro, fisica, 80).
calificacion(pedro, quimica, 45).
calificacion(pedro, literatura, 82).
calificacion(pedro, historia, 78).

calificacion(laura, matematicas, 98).
calificacion(laura, fisica, 94).
calificacion(laura, quimica, 91).
calificacion(laura, literatura, 90).
calificacion(laura, historia, 93).

calificacion(carlos, matematicas, 58).
calificacion(carlos, fisica, 60).
calificacion(carlos, quimica, 65).
calificacion(carlos, literatura, 70).
calificacion(carlos, historia, 75).

aprueba(Estudiante, Asignatura) :-
    calificacion(Estudiante, Asignatura, Puntuacion),
    Puntuacion >= 60.

asignaturas_aprobadas(Estudiante, TotalAprobadas) :-
    findall(Asignatura, aprueba(Estudiante, Asignatura), Asignaturas),
    length(Asignaturas, TotalAprobadas).

pasa_curso(Estudiante) :-
    asignaturas_aprobadas(Estudiante, TotalAprobadas),
    TotalAprobadas >= 3.

alumno_destacado(Estudiante) :-
    findall(Puntuacion, calificacion(Estudiante, _, Puntuacion), Puntuaciones),
    min_list(Puntuaciones, Minima),
    Minima >= 90.