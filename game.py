"""
메인 클래스가 있는 파일
"""

from guess import Guess 
from player1 import Player1  # player1: 컴퓨터
from player2 import Player2  # player2: 사용자
import time


class gameMain():
    name = input("이름을 입력하세요: ")  # 이름
    number = input("참가번호를 입력하세요: ")  # 참가번호
    totalNumberOfBeads = int(input("플레이할 구슬의 수를 입력하세요: "))  # 총 구슬의 개수
    player1 = Player1(totalNumberOfBeads)  # player1 정보 저장
    player2 = Player2(totalNumberOfBeads, name, number)  # player2 정보 저장
    guess = Guess()
    gameRound = 1  # 게임 판 수

    while 1:
        if gameRound % 2 == 1:  # 홀수 판: player2(사용자)-공격, player1(컴퓨터)-수비
            selectedBeads = player1.randomNumberOfBeads()  # player1(컴퓨터)-수비자.랜덤으로 구슬 고르기
            print(f"<<{gameRound}라운드>> 공격자입니다.")
            display = player1.messageOutput()  # player1이 수비자일 때 출력하는 메시지
            print(display)
            chosenEvenOdd = input()  # 사용자가 고른 홀/짝 String: "홀수" or "짝수"

            if guess.guess(selectedBeads, chosenEvenOdd):  # True일 때 = 사용자가 이겼을 때
                player1.subBeads(selectedBeads)  # player1 구슬 개수 감소
                player2.addBeads(selectedBeads)  # player2 구슬 개수 증가
                if guess.finished(player1.getNumOfBeads()):  # player1가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                    display = f"""
                              player1은 {selectedBeads}개의 구슬을 선택했습니다.
                              {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 성공입니다.
                              이번 판에서 {selectedBeads}개의 구슬을 얻었습니다.
                              플레이어1에게서 모든 구슬을 따냈으므로 승리입니다~~~!
                              """
                    print(display)
                    break
                else:  # 계속 게임 진행
                    display = f"""
                              player1은 {selectedBeads}개의 구슬을 선택했습니다.
                              {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 성공입니다.
                              이번 판에서 {selectedBeads}개의 구슬을 얻었습니다.
                              """
                    print(display)
                    # 결과 출력
                    print(player1.callResult())
                    print(player2.callResult())

                    gameRound += 1
                    continue

            else:  # False = 사용자가 졌다면
                player1.addBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                player2.subBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                if guess.finished(player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                    display = f"""
                              player1은 {selectedBeads}개의 구슬을 선택했습니다.
                              {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 실패입니다.
                              이번 판에서 {selectedBeads * 2}개의 구슬을 잃었습니다.
                              남은 구슬이 없으므로 패배입니다.....ㅠㅠ
                              """
                    print(display)
                    break

                else:  # 계속 게임 진행
                    display = f"""
                              player1은 {selectedBeads}개의 구슬을 선택했습니다.
                              {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 공격 실패입니다.
                              이번 판에서 {selectedBeads * 2}개의 구슬을 잃었습니다.
                              """
                    print(display)
                    # 결과 출력
                    print(player1.callResult())
                    print(player2.callResult())
                    gameRound += 1
                    continue

        else:  # 짝수 판: player1(컴퓨터)-공격, player2(사용자)-공격
            print(f"<<{gameRound}라운드>> 수비자입니다.")
            display = player2.messageOutput()  # player2가 수비자일 때 출력하는 메시지
            print(display)
            selectedBeads = int(input())  # 사용자가 건 구슬 수
            chosenEvenOdd = player1.randomChooseOddEven()  # player1(컴퓨터)-수비자. 홀수, 짝수 둘 중 하나 랜덤으로 고르기
            print("\t\tplayer1이 짝수/홀수를 고르는 중입니다. 잠시만 기다려주세요.")
            time.sleep(2)  # 2초 기다림

            if not guess.guess(selectedBeads, chosenEvenOdd):  # 사용자가 이겼을 때
                player1.subBeads(selectedBeads * 2)  # player1 구슬 개수 감소
                player2.addBeads(selectedBeads * 2)  # player2 구슬 개수 증가
                if guess.finished(player1.getNumOfBeads()):  # player1이 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 승리)
                    display = f"""
                              당신은 {selectedBeads}개의 구슬을 선택했습니다.
                              player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 성공입니다.
                              이번 판에서 {selectedBeads * 2}개의 구슬을 얻었습니다.
                              플레이어1에게서 모든 구슬을 따냈으므로 승리입니다~~~!
                              """
                    print(display)
                    break

                else:  # 계속 게임 진행
                    display = f"""
                              당신은 {selectedBeads}개의 구슬을 선택했습니다.
                              player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 성공입니다.
                              이번 판에서 {selectedBeads * 2}개의 구슬을 얻었습니다.
                              """
                    print(display)
                    # 결과 출력
                    print(player1.callResult())
                    print(player2.callResult())
                    gameRound += 1
                    continue

            else:  # False라면 = 사용자가 졌다면
                player1.addBeads(selectedBeads)  # player1 구슬 개수 감소
                player2.subBeads(selectedBeads)  # player2 구슬 개수 증가
                if guess.finished(player2.getNumOfBeads()):  # player2가 가지고 있는 구슬이 없을 경우 -> 게임 끝(player2의 패배)
                    display = f"""
                              당신은 {selectedBeads}개의 구슬을 선택했습니다.
                              player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 실패입니다.
                              이번 판에서 {selectedBeads}개의 구슬을 잃었습니다.
                              남은 구슬이 없으므로 패배입니다.....ㅠㅠ
                              """
                    print(display)
                    break
                else:  # 계속 게임 진행
                    display = f"""
                              당신은 {selectedBeads}개의 구슬을 선택했습니다.
                              player1은 {chosenEvenOdd}를 선택했으므로 참가번호 {number}번 {name}님의 수비 실패입니다.
                              이번 판에서 {selectedBeads}개의 구슬을 잃었습니다.
                              """
                    print(display)
                    # 결과 출력
                    print(player1.callResult())
                    print(player2.callResult())
                    gameRound += 1
                    continue


if __name__ == '__main__':
    gameMain()
