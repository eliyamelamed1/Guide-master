import React from 'react'

export default function Hero({childern, hero="defaultHero"}) {
    return <header className={hero}>{childern}</header>
}



// Unused

// Hero.defaulProps = {
//     hero: "defaultHero"
// };