import React from 'react';
import { useAtom } from 'jotai';
import { EleccionAtom } from '@/context/contex';

const Datos = () => {
  const [eleccion] = useAtom(EleccionAtom);

  if (!eleccion) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-lg text-gray-500">No hay datos disponibles para mostrar.</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center">
      <div className="w-full max-w-md bg-white rounded-lg shadow-md p-6  "
        style={{ marginTop: '1vh', background: 'rgba(0, 0, 0, 0.3)' }}
        >
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-white">Nombre de la Elección:</h2>
          <p className="text-gray-50">{eleccion.nombre}</p>
        </div>
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-white">Fecha de la Elección:</h2>
          <p className="text-gray-50">{eleccion.fecha}</p>
        </div>
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-white">Estado de la Elección:</h2>
          <p className="text-gray-50">{eleccion.estado_id || 'No definido'}</p>
        </div>
        <div className="mb-4">
          <h2 className="text-lg font-semibold text-white">Votos Permitidos:</h2>
          <p className="text-gray-50">{eleccion.votospermitidos}</p>
        </div>
      </div>
    </div>
  );
};

export default Datos;
