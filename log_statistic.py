def count_log_error(log_path):
    error_count=0
    error_content=[]
    with open(log_path,"r",encoding="utf-8") as f:
        for line_num,line in enumerate(f,1):
            if "ERROR" in line:
                error_count+=1
                error_content.append(f"No.{line_num}:{line.strip()}")