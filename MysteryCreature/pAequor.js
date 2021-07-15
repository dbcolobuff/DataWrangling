// Returns a random DNA base
  const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single stand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }
  const pAequorFactory = (num, dnaArray) => {
    return {
      specimenNum: num,
      dna: dnaArray,
      mutate () {
        for (let i = 0; i < this.dna.length; i++) {
          let newBase = returnRandBase()
          while (this.dna[i] === newBase) {
            newBase = returnRandBase()
          }
          this.dna[i] = newBase
        }
        return this.dna
      },
      compareDNA(pAequor) {
        let sameBase = 0
        for (let i = 0; i < pAequor.length; i++) {
          if (pAequor[i] === this.dna[i]) {
            sameBase += 1
          }
        }
        let fraction = sameBase/15
        let percentSimilar = fraction * 100
        console.log(`The two strands are ${percentSimilar}% similar.`)
      },
      willLikelySurvive () {
        let numCG = 0
        for (let i = 0; i < this.dna.length; i++) {
          if (this.dna[i] === 'C' || this.dna[i] === 'G') {
            numCG += 1
          }
        }
        let fracCG = numCG/15
        let percentCG = fracCG * 100
        if (percentCG >= 60) {
          return true
        } else {
          return false
        }
      }
    }
  }
  const makePool = () => {
    let pool = []
    let i = 1
    let getFish = pAequorFactory(i, mockUpStrand())
    while (i <= 30) {
      getFish = pAequorFactory(i, mockUpStrand())
      if (getFish.willLikelySurvive === true) {
        pool.push(getFish)
      }
    }
    return pool
  };
  
