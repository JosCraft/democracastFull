import React from 'react'
import { Button } from '@/components/ui/button';
import { Main } from '../template/main';
import logo from '@/assets/LOGO.png';
const Home = () => {
  return (
    <Main>
        <h1>DEMOCRACAST</h1>
        <p>Democracast is a platform that allows you to create and participate in polls in real time.</p>
        <Button>Get Started</Button>
    </Main>  
  )
}

export default Home