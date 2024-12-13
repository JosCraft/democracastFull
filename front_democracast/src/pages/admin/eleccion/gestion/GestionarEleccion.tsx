import React, { useEffect, useState } from 'react';
import { useAtom } from 'jotai'
import { EleccionAtom } from '@/context'
import { Main } from '@/template';
import { Eleccion } from '@/components';
import { TabsGestion } from './components';

const GestionarEleccion = () => {
  const [eleccion, setEleccion] = useAtom(EleccionAtom);

  useEffect(() => {
    const storedElecciones = localStorage.getItem('eleccion');
    if (storedElecciones) {
      setEleccion(JSON.parse(storedElecciones[0]) as Eleccion);
    }
  }, []);
  
  return (
    <Main>
      <div
        className="w-[90vw] h-[90vh] mx-auto p-10 rounded-lg shadow-md flex flex-col justify-center items-center"
        style={{ marginTop: "1vh", background: "rgba(149, 149, 149, 0.3)" }}
      >
        <h1 className="text-5xl font-bold text-amber-400 mb-6">Gestión de Elección</h1>
        <TabsGestion />
        {/* Verificar si eleccion existe antes de acceder a sus propiedades */}
        {eleccion ? (
          <p>{eleccion}</p>
        ) : (
          <p className="text-gray-500">No hay datos de elección disponibles</p>
        )}
      </div>
    </Main>
  );
};

export default GestionarEleccion;
