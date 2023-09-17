SELECT lang
  , COUNT(*) repos
  , ARRAY_AGG(STRUCT(name, stars) ORDER BY stars DESC LIMIT 20) repo
FROM (SELECT repo.name
    , MAX(CAST(JSON_EXTRACT_SCALAR(payload, '$.pull_request.base.repo.stargazers_count')AS INT64)) stars
    , JSON_EXTRACT_SCALAR(payload, '$.pull_request.base.repo.language') lang
  FROM `githubarchive.month.201912`  
  WHERE type='PullRequestEvent'
  GROUP by repo.name, lang)
where lang is not null and lang not in ('HTML', 'CSS', 'TypeScript')
GROUP BY lang
ORDER BY repos DESC
limit 5