import os
import sys

def search_skills(keywords):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
    skills_dir = os.path.join(base_dir, 'shared', 'skills')
    
    if not os.path.exists(skills_dir):
        # Fallback to output/shared/skills
        skills_dir = os.path.join(base_dir, 'output', 'shared', 'skills')
        if not os.path.exists(skills_dir):
            # Fallback to .agent/skills
            skills_dir = os.path.join(base_dir, '.agent', 'skills')

    if not os.path.exists(skills_dir):
        print(f"Error: Không tìm thấy thư mục skills ở {skills_dir}.")
        return

    results = []
    keywords_lower = [k.lower() for k in keywords]

    for skill_name in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill_name)
        skill_md = os.path.join(skill_path, 'SKILL.md')
        
        if os.path.isdir(skill_path) and os.path.isfile(skill_md):
            score = 0
            
            for kw in keywords_lower:
                if kw in skill_name.lower():
                    score += 5
            
            try:
                with open(skill_md, 'r', encoding='utf-8') as f:
                    content = ""
                    for i in range(20):
                        line = f.readline()
                        if not line:
                            break
                        content += line
                    
                    content_lower = content.lower()
                    for kw in keywords_lower:
                        if kw in content_lower:
                            score += 1
            except Exception:
                pass
                
            if score > 0:
                results.append({
                    'name': skill_name,
                    'path': skill_md,
                    'score': score
                })
                
    results.sort(key=lambda x: x['score'], reverse=True)
    
    if not results:
        print(f"Không tìm thấy kỹ năng nào phù hợp với các từ khóa: {', '.join(keywords)}")
        return
        
    print(f"Tìm thấy {len(results)} kỹ năng phù hợp. Hiển thị top 10:")
    print("-" * 50)
    for res in results[:10]:
        print(f"Skill: {res['name']}")
        print(f"Đường dẫn: {res['path']}")
        print(f"Độ liên quan: {res['score']}")
        print("-" * 50)
        print("Sử dụng tool 'view_file' với đường dẫn trên để đọc nội dung chi tiết.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Sử dụng: python search_skills.py <keyword1> <keyword2> ...")
        sys.exit(1)
        
    search_skills(sys.argv[1:])
