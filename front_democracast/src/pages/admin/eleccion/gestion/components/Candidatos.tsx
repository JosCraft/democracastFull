import React, { useState, useEffect} from 'react'
import { Button } from '@/components/ui'
import { Candidato } from '@/components/interface'
import  CardCandidato  from './CardCandidato'
import { IoIosPersonAdd } from "react-icons/io";
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

const Candidatos = () => {

  const [candidatosList, setCandidatosList] = useState<Candidato[]>(Listcandidatos)
    const handleClickOpen = () => {
        console.log('Agregar Candidato')
    }

    const handleRemoveCandidato = (id: number) => {
      setCandidatosList(candidatosList.filter((candidato) => candidato.id !== id));
  };

  return (
    <div>
        <Button className="bg-red-800 hover:bg-red-500" onClick={handleClickOpen}>
           <IoIosPersonAdd/>
            Agregar Candidato
        </Button>
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
