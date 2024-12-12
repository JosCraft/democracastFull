import { Main } from '@/template';
import { Eleccion, CardEleccion } from '@/components';
import { useEffect, useState } from 'react';
const elecciones: Eleccion[] = [
  {
    id: 1,
    nombre: 'Elección 1',
    fecha: '2022-12-12',
    estado_id: 1,
    votospermitidos: 5
  },
  {
    id: 2,
    nombre: 'Elección 2',
    fecha: '2022-12-12',
    estado_id: 1,
    votospermitidos: 1
  },
  {
    id: 3,
    nombre: 'Elección 3',
    fecha: '2022-12-12',
    estado_id: 1,
    votospermitidos: 1
  },
  {
    id: 4,
    nombre: 'Elección 4',
    fecha: '2022-12-12',
    estado_id: 1,
    votospermitidos: 3
  },
  {
    id: 5,
    nombre: 'Elección 5',
    fecha: '2022-12-12',
    estado_id: 1,
    votospermitidos: 4
  },
  {
    id: 6,
    nombre: 'Elección 6',
    fecha: '2022-12-12',
    estado_id: 2,
    votospermitidos: 2
  },
]



const Dashboard = () => {

  const [eleccions, setEleccions] = useState<Eleccion[]>([])

  useEffect(() => {
    setEleccions(elecciones)
  }, [])

  return (
    <Main>
      <div className="flex justify-center flex-wrap gap-5 mt-10 px-8">
        {eleccions.map((eleccion) => (
          <CardEleccion key={eleccion.id} eleccion={eleccion}  />
        ))}
      </div>
    </Main>  
  )
}

export default  Dashboard