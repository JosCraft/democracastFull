import {
  Card,
  CardFooter,
  CardContent,
  CardHeader,
  CardTitle,
} from "../ui/card"
import { Button } from "../ui/button"
import { Eleccion } from "../interface"
import { useEffect, useState } from 'react'
import  ParticiparButton  from './ParticiparButton'

interface CardEleccionProps {
  eleccion: Eleccion

}

const CardEleccion = ({eleccion}:CardEleccionProps) => {


  const [checkRol, setCheckRol] = useState(false);


  useEffect(() => {
    if (localStorage.getItem('rol') === 'admin') {
      setCheckRol(true)
    }
  }, [])

  return (
<Card className="w-[300px] p-6 shadow-xl border rounded-lg bg-amber-100 flex flex-col items-start">
  <CardHeader className="mb-4 flex items-center justify-between w-full">
    <CardTitle className="text-xl font-semibold text-slate-800">{eleccion.nombre}</CardTitle>
    {eleccion.estado_id === 1 ? (
      <span className="ml-2 bg-green-600 text-amber-50 px-3 py-1 rounded-full text-sm font-medium">
        Activa
      </span>
    ) : (
      <span className="ml-2 bg-red-600 text-amber-50 px-3 py-1 rounded-full text-sm font-medium">
        Inactiva
      </span>
    )}
  </CardHeader>
  <CardContent className="space-y-2 text-slate-700">
    <p className="text-sm">
      Fecha: <span className="font-medium text-slate-800">{eleccion.fecha}</span>
    </p>
    <p className="text-sm">
      Votos Permitidos:{" "}
      <span className="font-medium text-slate-800">{eleccion.votospermitidos}</span>
    </p>
  </CardContent>
  <CardFooter className="mt-4 w-full flex justify-end">
    {checkRol ? (
      <Button className="bg-amber-600 text-white hover:bg-red-700 px-4 py-2 rounded-md">
        Gestionar
      </Button>
    ) : (
      eleccion.estado_id === 1 ? (
        <ParticiparButton id={(eleccion.id || 0).toString()} cantidadVotos={eleccion.votospermitidos} />
      ) : null
    )}
  </CardFooter>
</Card>
  )
}

export default CardEleccion
