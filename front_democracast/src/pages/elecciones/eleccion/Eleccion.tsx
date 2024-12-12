import React, { useState, useEffect } from 'react'
import { Candidato } from "@/components/interface"
import {CardCandidatos, AlertEleccion}  from './components'
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

const Eleccion = ({ idEleccion }: EleccionProps) => {
    const [candidatosList, setCandidatos] = useState<Candidato[]>([]);
    const [cantidadVotos, setCantidadVotos] = useState<number>(0);
    const [maxVotos, setMaxVotos] = useState<number>(0);
    const [isAlertOpen, setIsAlertOpen] = useState<boolean>(false);
  
    const handleVotar = (candidato: Candidato) => {
      setCantidadVotos(cantidadVotos + 1);
  
      if (cantidadVotos + 1 >= maxVotos) {
        setIsAlertOpen(true);
      }
    };
  
    const handleCloseAlert = () => {
      setIsAlertOpen(false);
      setCantidadVotos(0); 
    };
  
    useEffect(() => {
      setCandidatos(candidatos.filter((candidato) => candidato.eleccion_id === idEleccion));
      const storedMaxVotos = localStorage.getItem("cantidadVotos");
      setMaxVotos(storedMaxVotos ? parseInt(storedMaxVotos) : 0);
    }, [idEleccion]);
  
    return (
      <Main>
        <div className="flex justify-center flex-wrap gap-4 mt-10 px-8">
          {cantidadVotos < maxVotos ? (
            <>
              {candidatosList.map((candidato) => (
                <CardCandidatos key={candidato.id} candidato={candidato} handleVotar={handleVotar} />
              ))}
            </>
          ) : (
            <p className="text-center text-xl text-gray-600">Ya no puedes votar más.</p>
          )}
        </div>
  
        <AlertEleccion isOpen={isAlertOpen} onClose={handleCloseAlert} />
      </Main>
    );
  };
  
  export default Eleccion;