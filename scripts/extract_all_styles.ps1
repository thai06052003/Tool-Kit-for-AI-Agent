$url = 'https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/README.md'
$content = Invoke-WebRequest -Uri $url | Select-Object -ExpandProperty Content
$lines = $content -split '\r?\n'
$collect = $false
$styles = @()
foreach ($line in $lines) {
    if ($line -match '^## ') { 
        $collect = $true
        $category = $line.Replace('## ', '').Trim() 
    }
    if ($collect -and ($line -match '^- \[.*?\]\((.*?)\)')) {
        $startIndex = $line.IndexOf('[') + 1
        $endIndex = $line.IndexOf(']')
        if ($startIndex -gt 0 -and $endIndex -gt $startIndex) {
            $name = $line.Substring($startIndex, $endIndex - $startIndex).Trim()
            $styles += [PSCustomObject]@{ Category = $category; Name = $name }
        }
    }
}
$styles | Export-Csv -Path 'all_styles.csv' -NoTypeInformation
$styles | Format-Table -AutoSize
