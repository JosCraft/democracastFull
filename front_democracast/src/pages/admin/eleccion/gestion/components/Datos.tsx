import React from 'react'
import { useAtom } from 'jotai'
import { EleccionAtom } from '@/context'
import { Eleccion } from '@/components'



const Datos = () => {
    const [eleccion] = useAtom(EleccionAtom);
  return (
    <div>
    </div>
  )
}

export default Datos
