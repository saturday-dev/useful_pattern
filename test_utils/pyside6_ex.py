from PySide6.QtWidgets import QApplication, QWidget

# CLI 환경에서 매개변수를 사용하기 위해 필요합니다.
import sys

# 앱 한 개당 오직 하나의 QApplication만 필요합니다.
# sys.argv를 적용하면 CLI 환경에서 매개변수를 허용할 수 있습니다.
# Command Line의 매개변수가 필요 없다면, QApplication([]) 이렇게 사용하셔도 좋습니다.
app = QApplication(sys.argv)

# 우리의 Window가 되어 줄 Qt 위젯을 만들어 봅시다. 
window = QWidget()
window.show() # 주의!!! window는 숨김(hidden) 상태가 디폴트 입니다.

# 이벤트 루프를 시작합니다.
app.exec_()

# 앱을 종료하고 이벤트 루프가 멈추기 전엔 이 밑의 어떤 코드도 실행되지 않을 것 입니다.