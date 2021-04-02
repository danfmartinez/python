import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Time
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumno'

    id = Column(Integer, Sequence('alumno_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    curso_id = Column(Integer, ForeignKey('curso.id'))
   
    curso = relationship("Curso", back_populates= "alumnos")

    def __repr__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Curso(Base):
    __tablename__ = 'curso'

    id = Column(Integer, Sequence('curso_id_seq'), primary_key=True)
    nombre = Column(String)

    alumnos = relationship("Alumno", back_populates= "curso")
    horarios = relationship("Horario", back_populates= "curso")

    def __repr__(self):
        return "{}".format(self.nombre)

class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, Sequence('profesor_id_seq'), primary_key=True)
    nombre = Column(String)
    apellido = Column(String)

    horarios = relationship("Horario", back_populates= "profesor")

    def __repr__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Horario(Base):
    __tablename__ = 'horario'

    id = Column(Integer, Sequence('horario_id_seq'), primary_key=True)
    dia_semana = Column(String)        
    hora_desde = Column(Time)
    hora_hasta = Column(Time)

    curso_id = Column(Integer, ForeignKey('curso.id'))
    profesor_id = Column(Integer, ForeignKey('profesor.id'))

    curso = relationship("Curso", back_populates= "horarios")
    profesor = relationship("Profesor", back_populates= "horarios")

    def __repr__(self):
        return "{} {} {}".format(self.dia_semana,self.hora_desde, self.hora_hasta)


###########################

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

curso1 = Curso(nombre= "A1")
curso2 = Curso(nombre= "A2")

alumno1 = Alumno(nombre= "Carolina", apellido= "Aranda", curso= curso1)
alumno2 = Alumno(nombre= "Juan", apellido= "Moreno", curso= curso1)
alumno3 = Alumno(nombre= "Alejandro", apellido= "Martinez", curso = curso2)
alumno4 = Alumno(nombre= "Daniela", apellido= "Mendoza", curso= curso1)
alumno5 = Alumno(nombre= "Luisa", apellido= "Rodriguez", curso= curso2 )
alumno6 = Alumno(nombre= "Arturo", apellido= "Duque", curso= curso2)

profesor1 = Profesor(nombre= "Daniel", apellido = "Martinez",)
profesor2 = Profesor(nombre= "Cesar", apellido = "Moreno")

hora1 = datetime.time(7,0)
hora2 = datetime.time(9,0)
hora3 = datetime.time(11,0)
horario1 = Horario(dia_semana= "Lunes", hora_desde= hora1, hora_hasta= hora2, curso= curso1, profesor= profesor1 )
horario2 = Horario(dia_semana= "Lunes", hora_desde= hora1, hora_hasta= hora2, curso= curso2, profesor= profesor2 )
horario3 = Horario(dia_semana= "Martes", hora_desde= hora2, hora_hasta= hora3, curso= curso1, profesor= profesor2 )
horario4 = Horario(dia_semana= "Martes", hora_desde= hora2, hora_hasta= hora3, curso= curso2, profesor= profesor1 )

session.add(curso1)
session.add(curso2)

session.add(alumno1)
session.add(alumno2)
session.add(alumno3)
session.add(alumno4)
session.add(alumno5)
session.add(alumno6)

session.add(profesor1)
session.add(profesor2)

session.add(horario1)
session.add(horario2)
session.add(horario3)
session.add(horario4)

session.commit()
