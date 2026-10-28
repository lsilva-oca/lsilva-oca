# Publicar el perfil de Leandro

La versión principal está preparada para `leeansilva` y enlaza la cuenta laboral `lsilva-oca`.

Repositorio de alojamiento en OCA: `git@github-oca:lsilva-oca/leeansilva.git`.
Ese nombre aloja el proyecto, pero no activa el README de perfil de `lsilva-oca`: para eso el repositorio debe llamarse `lsilva-oca/lsilva-oca`. Para el perfil personal, usar `leeansilva/leeansilva`.

1. Crear o usar el repositorio público `leeansilva/leeansilva`.
2. Copiar `README.md`, `assets/`, `scripts/` y `.github/` a ese repositorio.
3. En GitHub Actions, ejecutar **Profile cards** para regenerar estadísticas y banners. El workflow también corre diariamente y usa el token automático de GitHub.
4. Si las políticas del repositorio lo requieren, habilitar permisos de escritura para GitHub Actions. El workflow declara `contents: write`.

Las tarjetas muestran estadísticas de la cuenta personal, sin sumar la cuenta OCA. Sin un token personal, se muestran repositorios públicos, estrellas y seguidores. `METRICS_TOKEN` es opcional para contribuciones y rachas; no es necesario para publicar el perfil. Nunca poner tokens en archivos.

El workflow **Metrics** quedó manual y requiere `METRICS_TOKEN`; sus imágenes no se usan en este README.

Para regenerar el banner localmente: `py scripts/profile_banner.py`.
Para actualizar tarjetas: `py scripts/cards.py --user leeansilva --projects assets/projects.json --out assets`.
Para revisar la presentación: abrir `preview.html`. En VS Code, la vista previa de `README.md` permite revisar el Markdown.

El banner actual incorpora el retrato de Leandro como SVG inline: no depende de imágenes externas para mostrar la foto. Los banners v9 y radares originales se conservaron como referencia y no se usan en el README. No ejecutar el generador antiguo `scripts/banner/generate.py` para actualizar el banner de Leandro.

Para regenerar el retrato, instalar Pillow y ejecutar `py scripts/dotify.py assets/source/lean-cutout.png -o assets/portrait --cols 80 --cell 4 --detail 0.5 --contrast 1.15 --gamma 0.65 --reveal --reveal-time 1.8 --dot-scale 0.86`. Luego ejecutar `py scripts/profile_banner.py`. La foto original no se copia al repositorio; se conserva el recorte transparente en assets/source/lean-cutout.png.

La biografía, stack y selección de proyectos se adaptaron de https://leandro-silva.vercel.app/.
