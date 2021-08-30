const moods = {
  fantastic: "Yay! That's so awesome!",
  great: "That's great to hear!",
  good: "I'm glad you're doing well.",
  neutral: "That's better than not okay, so I'm glad!",
  down: "That's understandable, we all have those days.",
  annoyed: "That sounds frustrating.",
  overwhelmed: "Take one step at a time and take deep breaths. Everything is going to be okay.",
}

function showHideReaction(mood) {
  var checkedMood = document.getElementById(`checkbox-${mood}`)
  var reactionText = document.getElementById('reaction-text')
  reactionText.innerHTML = moods[mood]
}