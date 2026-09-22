import React from 'react'

const JobCard = ({company,featured,position, role, level, postedAt, contract, location, languages, tools}) => {
  const tags = [position, level, ...languages, ...tools]
  return (
    <section className='jobCard'>
        <div className='logoWrapper'></div>
        <div>
            <header>
                {company}
                {featured && <span>FEATURED</span>}
            </header>
            <h2>{level} {position} {role}</h2>
            <div className='details'>
                <span>{(new Date(postedAt)).toLocaleDateString()}</span>
                <span>{contract}</span>
                <span>{location}</span>
            </div>
        </div>
        <div className='tags'>
            {tags.map(tag => <span>{tag}</span>)}
        </div>
    </section>
  )
}

export default JobCard