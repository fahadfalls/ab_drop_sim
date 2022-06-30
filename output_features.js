console.log('tokenData.hash = %s\ntokenData.tokenId = %s\n', tokenData.hash, tokenData.tokenId);

let feats = calculateFeatures(tokenData);

for (const [key, val] of Object.entries(feats)) {
  console.log('%s: %s', key, val);
}