## 회사코드 기준으로 데이터프레임 형태 바꾸기
## companyguide 재무제표 사용

def change_df(firm_code, dataframe):
    
    for num, col in enumerate(fs_df.columns):    # 칼럼수만큼 반복
        temp_df = pd.DataFrame({code:fs_df[col]})    # 해당칼럼(날짜)만 포함된 새로운 데이터 프레임 생성
        temp_df = temp_df.T    #데이터 프레임의 열과 행을 바꿈
        temp_df.columns = [[col]*len(fs_df),temp_df.columns]    # 위쪽엔 날짜를 칼럼길이만큼 반복하고, 아래엔 기존의 칼럼
        if num ==0:
            total_df = temp_df # 종료
        else:
            total_df = pd.merge(total_df,temp_df,how='outer',left_index=True,right_index=True) # 데이터 프레임 합침
        
        return total_df