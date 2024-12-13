export interface Candidato {
    id?: number
    numero_cartelera: number
    cantidad_votos: number
    eleccion_id: number
    persona_id: number
    nombre: string
}

export interface Persona
{
    id?: number
    nombre: string
    apellido: string
}