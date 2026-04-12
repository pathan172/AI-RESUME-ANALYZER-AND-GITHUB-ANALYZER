from app import fetch_github_data, analyze_repos, analyze_repo_quality, analyze_activity, categorize_projects, generate_ai_suggestions

user_data, repo_data = fetch_github_data('octocat')
print('user keys', list(user_data.keys())[:10])
print('repos type', type(repo_data), 'len', len(repo_data))
stats = analyze_repos(repo_data)
print('stats', stats)
quality_stats = analyze_repo_quality(repo_data)
print('quality', quality_stats)
activity_stats = analyze_activity(repo_data)
print('activity', activity_stats)
categories = categorize_projects(repo_data)
print('categories counts', {k: len(v) for k,v in categories.items()})
print('suggestions', generate_ai_suggestions(stats, quality_stats, activity_stats, categories))
