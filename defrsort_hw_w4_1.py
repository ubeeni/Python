# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:31:43 2020

@author: yubin
"""

def rsort(th):                                  # rsort라는 함수를 선언한다.
    return sorted(th, key=th.get, reverse=True) # (return 뒤에) 넘겨줄 자료를 적는다. 
# dict형 변수를 정렬할 경우 키값을 기준으로 정렬하기 위해선 sorted 메소드를 사용하면 된다. 
# sorted 안에 key 값을 설정하지 않을 경우 기본적으로 키값을 기준으로 정렬하게 되며, reverse 옵션을 주지 않으면 작은 것부터 큰 것 순으로 정렬된다.
# sorted()라는 내장함수를 사용하면 list 형태로 sort된 값을 반환한다.(sorted()는 이터러블 객체(순회가능한 자료형)로부터 정렬된 리스트를 생성하기 때문에 기존의 리스트를 변경하는 것이 아니라 정렬된 새로운 리스트를 반환해준다.)
# rsort 함수의 목적은 th={}라는 dictionary의 value로 sorting을 한 key값을 뽑아내고자 하는 것이다.
# "reverse = True"를 사용하면 내림차순으로 정렬시켜 준다. 
dhash = {}                                      # 딕셔너리를 선언한다.
fp = open("data_log.csv","r",encoding="UTF8")   # data_log.csv 파일을 읽기모드로 오픈한다.
for line in fp:                                 # 파일의 각 줄을 살펴본다.
                                                # "for 변수 in 파일 변수:"라는 의미로 파일(fp)에 들어있는 내용을 한 줄씩 읽어들여서 명령어를 처리한다.
                                                # for문을 사용해서 파일에 들어있는 내용을 다 읽을 때까지 반복한다.
    line = line.strip("\r\n")                   # strip 명령어를 사용해서 개행문자를 자른다.
    psd = line.split(",")                       # split 명령어를 사용해서 텍스트를 자른다.(콤마로 문자열 분리한 후 list로 저장)
                                                # 리스트 = 문자열변수.split("구분자")
    query = psd[1]                              # query는 psd 리스트(ip,*검색어,시간,device)에 있는 2번째 값을 의미한다는 뜻이다.

    if not query in dhash:                      # 딕셔너리를 초기화한다.
        dhash[query] = 0                        # query가 이미 딕셔너리 안에 있는지 확인해서 없다면 그 query에 대해서 값을 0으로 초기화 해주는 작업이 필요하다.         
        
    dhash[query] += 1                           # 딕셔너리 값을 증가한다.(query에 대해서 키워드가 한번 나올때마다 1씩 증가)
    
fp.close()                                      # 파일을 닫는다.

sorted_list = rsort(dhash)                      # sorted_list는 매개변수가 dhash인 rsort 함수임을 의미한다.
for query in sorted_list:                       # sorted_list 안에 있는 query를 반복적으로 보고 싶은 것이다.(sorted_list에 순차적으로 접근이 가능하기 때문이다.)       
    print(query,dhash[query])                   # 딕셔너리 값을 출력한다.
                                                # 순차적으로 딕셔너리에 저장되었던 query들이 출력된다. key(query)에 대한 value를 딕셔너리에서 보여준다.
