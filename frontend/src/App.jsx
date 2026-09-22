import { useEffect, useState } from "react"
import { getJobs } from "./services/api"

const App = () => {
  const [jobs, setJobs] = useState()

  useEffect(()=>{
    getJobs().then(data => setJobs(data))
  })

  if(jobs == undefined) return <div>Loading...</div>

  return (
    <div>
      {jobs.map(job => <h1>{job.company}</h1>)}
    </div>
  )
}

export default App