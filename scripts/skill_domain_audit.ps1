function Get-SkillDomain($path) {
    if (-not (Test-Path $path)) { return 'Missing' }
    $content = Get-Content $path -Raw
    if ($content -match 'frontend|ui|ux|css|react|tailwind|design|responsive') { return 'Frontend/UI' }
    if ($content -match 'backend|dotnet|csharp|api|node|sql|database|efcore') { return 'Backend' }
    if ($content -match 'security|audit|vulnerability|auth|owasp') { return 'Security' }
    if ($content -match 'test|qa|playwright|xunit|tdd') { return 'Testing' }
    if ($content -match 'devops|docker|ci/cd|deploy') { return 'DevOps' }
    return 'General'
}

$ideFolders = @('.agent', '.cursor', '.github', '.kiro', '.opencode', '.vs')
$report = @()

foreach ($ide in $ideFolders) {
    $skillsPath = Join-Path $ide 'skills'
    if (Test-Path $skillsPath) {
        $skills = Get-ChildItem -Path $skillsPath -Directory
        foreach ($s in $skills) {
            $domain = Get-SkillDomain -path (Join-Path $s.FullName 'SKILL.md')
            $report += [PSCustomObject]@{ IDE = $ide; Skill = $s.Name; Domain = $domain }
        }
    }
}

$report | Group-Object IDE, Domain | Select-Object Name, Count | Sort-Object Name | Format-Table -AutoSize
