import React from 'react'
import { Button } from '@/components/ui'

const Candidatos = () => {

    const handleClickOpen = () => {
        console.log('Agregar Candidato')
    }

  return (
    <div>
        <Button variant="contained" color="primary" onClick={handleClickOpen}>
            Agregar Candidato
        </Button>
        <div>
            
        </div>
    </div>
  )
}

export default Candidatos
