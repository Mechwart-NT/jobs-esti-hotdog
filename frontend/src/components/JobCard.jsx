import React from 'react'

const JobCard = ({company,featured,position, role, level, postedAt, contract, location, languages, tools}) => {
  const tags = [position, level, ...languages, ...tools]
  return (
    <section>
        <div className='logoWrapper'></div>
        <div>
            <header>
                {company}
                {featured && <span>FEATURED</span>}
            </header>
            <h2>{level} {position} {role}</h2>
            <div>
                <span>{postedAt}</span>
                <span>{contract}</span>
                <span>{location}</span>
            </div>
        </div>
        <div>

        </div>
    </section>
  )
}

export default JobCard