import { useEffect, useState } from "react"
import { getJobs } from "./services/api"
import JobCard from "./components/JobCard"

const App = () => {
  const [jobs, setJobs] = useState([])

  useEffect(()=>{
    getJobs().then(data => setJobs(data))
  })

  return (
    <div>
      {jobs.map(job => <JobCard {...job}/>)}
    </div>
  )
}

export default App