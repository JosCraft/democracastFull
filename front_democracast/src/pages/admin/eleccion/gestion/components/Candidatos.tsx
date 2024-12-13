import React, { useState, useEffect} from 'react'
import { Candidato, Persona } from '@/components/interface'
import  CardCandidato  from './CardCandidato'
import { DialogCandidato } from './DialogCandidato'
const Listcandidatos: Candidato[] = [
  {
      id: 1,
      numero_cartelera: 1,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 1,
      nombre: 'Candidato 1'
  },
  {
      id: 2,
      numero_cartelera: 2,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 2,
      nombre: 'Candidato 2'
  },
  {
      id: 3,
      numero_cartelera: 3,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 3,
      nombre: 'Candidato 3'
  },
  {
      id: 4,
      numero_cartelera: 4,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 4,
      nombre: 'Candidato 4'
  },
  {
      id: 5,
      numero_cartelera: 5,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 5,
      nombre: 'Candidato 5'
  },
  {
      id: 6,
      numero_cartelera: 6,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 6,
      nombre: 'Candidato 6'
  },
  {
      id: 7,
      numero_cartelera: 7,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 7,
      nombre: 'Candidato 7'
  },
  {
      id: 8,
      numero_cartelera: 8,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 8,
      nombre: 'Candidato 8'
  },
  {
      id: 9,
      numero_cartelera: 9,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 9,
      nombre: 'Candidato 9'
  },
  {
      id: 10,
      numero_cartelera: 10,
      cantidad_votos: 0,
      eleccion_id: 1,
      persona_id: 10,
      nombre: 'Candidato 10'
  },
]

const Listpersonas: Persona[] = [
    {
        id: 1,
        nombre: 'Persona 1',
        apellido: 'Apellido 1',
    },
    {
        id: 2,
        nombre: 'Persona 2',
        apellido: 'Apellido 2'
    },
    {
        id: 3,
        nombre: 'Persona 3',
        apellido: 'Apellido 3'
    },
    {
        id: 4,
        nombre: 'Persona 4',
        apellido: 'Apellido 4'
    },
    {
        id: 5,
        nombre: 'Persona 5',
        apellido: 'Apellido 5'
    },
    {
        id: 6,
        nombre: 'Persona 6',
        apellido: 'Apellido 6'
    },
    {
        id: 7,
        nombre: 'Persona 7',
        apellido: 'Apellido 7'
    },
    {
        id: 8,
        nombre: 'Persona 8',
        apellido: 'Apellido 8'
    },
    {
        id: 9,
        nombre: 'Persona 9',
        apellido: 'Apellido 9'
    },
    {
        id: 10,
        nombre: 'Persona 10',
        apellido: 'Apellido'
    }
]


const Candidatos = () => {

  const [candidatosList, setCandidatosList] = useState<Candidato[]>(Listcandidatos)
    const [personas, setPersonas] = useState<Persona[]>(Listpersonas)

    const handleClickOpen = () => {
        console.log('Agregar Candidato')
    }

    const handleRemoveCandidato = (id: number) => {
      setCandidatosList(candidatosList.filter((candidato) => candidato.id !== id));
  };

 const agregarCandidato = (persona: Persona) => {

 }
 const registrarPersona = (persona: Persona) => {

 } 

  return (
    <div>
        <DialogCandidato 
            personas={personas}
            agregarCandidato={agregarCandidato}
            registrarPersona={registrarPersona}
        />
        <div
            className="flex justify-center flex-wrap gap-4 mt-10 px-8 overflow-y-auto"
            style={{ maxHeight: '400px' }}
        >
            {candidatosList && candidatosList.length > 0 ? (
                <>
                    {candidatosList.map((candidato) => (
                        <CardCandidato key={candidato.id} candidato={candidato} handleRemoveCandidato={handleRemoveCandidato} />
                    ))}
                </>
            ) : (
                <p className="text-center text-xl text-gray-600">No hay Candidatos</p>
            )}
        </div>
    </div>
  )
}

export default Candidatos
