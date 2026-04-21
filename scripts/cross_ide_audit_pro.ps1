$ides = @('.agent', '.cursor', '.github', '.kiro', '.opencode', '.vs')
$paths = @('agents', 'skills', 'rules', 'workflows', 'hooks', 'steering')

$results = @()

foreach ($ide in $ides) {
    $row = [ordered]@{ IDE = $ide }
    foreach ($p in $paths) {
        $fullPath = Join-Path $ide $p
        if (Test-Path $fullPath) {
            $count = (Get-ChildItem -Path $fullPath -Recurse -File).Count
            $row[$p] = $count
        } else {
            $row[$p] = 0
        }
    }
    
    # Check for instruction files at root of IDE folders
    $instrFiles = Get-ChildItem -Path $ide -File | Where-Object { $_.Name -match 'instructions|AGENTS' }
    $row['Instructions'] = $instrFiles.Count

    $results += [PSCustomObject]$row
}

$results | Format-Table -AutoSize
