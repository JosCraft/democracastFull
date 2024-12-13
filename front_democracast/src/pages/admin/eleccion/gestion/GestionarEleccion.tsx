import React, { useEffect, useState } from 'react';
import { useAtom } from 'jotai';
import { EleccionAtom } from '../../../../context/contex';
import { Main } from '@/template';
import { TabsGestion } from './components';

interface Eleccion {
  id: string;
  nombre: string;
  fecha: string;
  estado_id?: string;
  votospermitidos: number;
}

const GestionarEleccion = () => {
  const [, setEleccionGlobal] = useAtom(EleccionAtom);
  const [eleccion, setEleccion] = useState<Eleccion | null>(null);

  useEffect(() => {
    const storedElecciones = localStorage.getItem('eleccion');

    if (storedElecciones) {
      try {
        const parsedElecciones = JSON.parse(storedElecciones);

        const eleccionData: Eleccion = {
          id: parsedElecciones.id,
          nombre: parsedElecciones.nombre,
          fecha: parsedElecciones.fecha,
          estado_id: parsedElecciones.estado_id,
          votospermitidos: parsedElecciones.votos_permitidos,
        };

        setEleccion(eleccionData);
        setEleccionGlobal(eleccionData);
      } catch (error) {
        console.error('Error al parsear el JSON:', error);
      }
    }
  }, [setEleccionGlobal]);

  return (
    <Main>
      <div
        className="w-[90vw] h-[90vh] mx-auto p-10 rounded-lg shadow-md flex flex-col justify-center items-center"
        style={{ marginTop: '1vh', background: 'rgba(149, 149, 149, 0.3)' }}
      >
        <h1 className="text-5xl font-bold text-amber-400 mb-6">Gestión de Elección</h1>
        {eleccion ? (
          <>
            <TabsGestion />
          </>
        ) : (
          <p className="text-lg text-white">Cargando datos de la elección...</p>
        )}
      </div>
    </Main>
  );
};

export default GestionarEleccion;
