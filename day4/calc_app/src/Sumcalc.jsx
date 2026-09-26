import { useState } from "react"
export default function Sumcalc() {
    const[num1,setNum1] = useState(0);
    const[num2,setNum2] = useState(0);
    const[sum,setSum] = useState(0);

  return(
    <>
     this is not the sum calculator
     <p>Number: <input type="number" value={num1} onChange={(e) => {setNum1(parseInt(e.target.value));}} /></p>
     <p>Number: <input type="number" value={num2} onChange={(e) => {setNum2(parseInt(e.target.value));}} /></p>
    <p><button onClick={() => {setSum(num1 + num2);}}>Calculate Sum</button></p>
     
     <p>Sum of {num1} and {num2} is {sum}</p>
    </>
  )
}