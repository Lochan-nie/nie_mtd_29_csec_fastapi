import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import About from './about'
import Square from './square'
import Sumcalc from './Sumcalc'



function App() {
  

  return (

  <div>
    <p>Welcome to the Calculator App!</p>
    <hr></hr> 
    <Square />
    <hr></hr>
    <Sumcalc />
  </div>
    
  )
}

export default App
