import ScriptX from 'vue-scriptx'

import Ads from 'vue-google-adsense'

export default boot(async ({ app }) => {
  app.use(ScriptX)
  app.use(Ads.AutoAdsense, { adClient: 'ca-pub-5504503922827317', isNewAdsCode: true })
});



// import Vue from 'vue'
// import Ads from 'vue-google-adsense'

// Vue.use(require('vue-script2'))

// Vue.use(Ads.AutoAdsense, { adClient: 'ca-pub-5504503922827317' })
