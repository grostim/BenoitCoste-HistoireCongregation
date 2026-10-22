-- Le lien textuel accompagne déjà le QR code dans la version Markdown.
function Image(image)
  if image.src == "images/signaler-erreur.png" then
    return {}
  end
end
