import QtQuick 2.15
import QtGraphicalEffects 1.15

import org.kde.plasma.core 2.0 as PlasmaCore

Item {
  id: root

  Rectangle {
    id: background

    anchors.fill: parent

    color: '#000000'
  }

  property int stage

  onStageChanged: {
    // This code is little tricky and not working on small screen. Fix it later.
    // progressAnimation.from = progress.getWidth();
    // progressAnimation.to = progress.getWidth() + 100;
    // progressAnimation.duration = 1000;
    // progressAnimation.restart();
  }

  Image {
    id: logo

    anchors.horizontalCenter: background.horizontalCenter
    y: (background.height - this.height) / 2
    width: background.height / 4.21875 // 256 when SCREEN_WIDTHx1080
    height: background.height / 4.21875 // 256 when SCREEN_WIDTHx1080

    source: 'images/logo.svg'
  }

  Rectangle {
    id: progressBackground

    anchors.horizontalCenter: background.horizontalCenter
    y: logo.y + logo.height + 100

    width: background.width / 2.5
    height: 8

    color: '#4d4d4d'
    radius: 100

    layer.enabled: true
    layer.effect: OpacityMask {
      maskSource: Rectangle {
        x: progressBackground.x
        y: progressBackground.y
        width: progressBackground.width
        height: progressBackground.height

        radius: progressBackground.radius
      }
    }

    Rectangle {
      id: progress

      width: getWidth()
      height: progressBackground.height

      color: '#ffffff'

      DropShadow {
        anchors.fill: progress
        radius: 8
        color: '#80000000'
        source: progress
      }

      function getWidth() {
        if (stage === 0) {
          return 0;
        }

        return (stage / 6) * progressBackground.width;
      }
    }
  }

  // Unused yet.
  NumberAnimation {
    id: progressAnimation

    target: progress
    property: 'width'
  }
}
