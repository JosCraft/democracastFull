import React, { useState, useEffect } from 'react'
import { Candidato } from "@/components/interface"
import CardCandidatos  from './components/CardCandidatos'
import { Main } from '@/template';

const candidatos: Candidato[] = [
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

interface EleccionProps {
    idEleccion ?: number
}

const Eleccion = (
    {idEleccion}: EleccionProps
) => {
    console.log(idEleccion)
    const [candidatosList, setCandidatos] = useState<Candidato[]>([])
    const handleVotar = (candidato: Candidato) => {
        console.log(candidato)
    }

    useEffect(() => {
        setCandidatos(candidatos.filter(candidato => candidato.eleccion_id === idEleccion))
    }, [candidatos])

  return (
    <Main>
        <div className='flex justify-center flex-wrap gap-5 mt-10 px-8'>
        {candidatosList.map((candidato) => (
            <CardCandidatos key={candidato.id} candidato={candidato} handleVotar={handleVotar} />
        ))}
        </div>
    </Main>
  )
}

export default Eleccion
